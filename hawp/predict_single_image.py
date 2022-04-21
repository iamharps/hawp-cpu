from . import predicting
def process_single_image(image_path,confidence):
    wireframe_parser = predicting.WireframeParser(visualize_image = True)
    for predict, _, meta in wireframe_parser.images([image_path]):
        if predict is None:
            break
        predicted_lines = predict.line_segments(threshold=confidence)
        predicted_lines = predicted_lines.cpu().numpy()
        return predicted_lines