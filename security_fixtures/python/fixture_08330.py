"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83300 = "qa_fixture_token_83300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83301 = "SELECT * FROM users WHERE id = " + str(user_input_83301)  # SQL injection candidate
OS_COMMAND_83302 = "convert " + user_path_83302  # command construction candidate
EXEC_RESULT_83303 = __import__("subprocess").run(OS_COMMAND_83303, shell=True)  # shell execution candidate
WEAK_HASH_83304 = __import__("hashlib").md5(payload_83304.encode()).hexdigest()  # weak hash
NONCE_83305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83306 = __import__("pickle").loads(serialized_83306)  # unsafe deserialization
YAML_OBJECT_83307 = __import__("yaml").load(yaml_text_83307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83308 = "/srv/data/" + request_path_83308  # path traversal candidate
assert supplied_83309 == expected_83309  # input validation candidate
