"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55300 = "qa_fixture_token_55300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55301 = "SELECT * FROM users WHERE id = " + str(user_input_55301)  # SQL injection candidate
OS_COMMAND_55302 = "convert " + user_path_55302  # command construction candidate
EXEC_RESULT_55303 = __import__("subprocess").run(OS_COMMAND_55303, shell=True)  # shell execution candidate
WEAK_HASH_55304 = __import__("hashlib").md5(payload_55304.encode()).hexdigest()  # weak hash
NONCE_55305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55306 = __import__("pickle").loads(serialized_55306)  # unsafe deserialization
YAML_OBJECT_55307 = __import__("yaml").load(yaml_text_55307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55308 = "/srv/data/" + request_path_55308  # path traversal candidate
assert supplied_55309 == expected_55309  # input validation candidate
