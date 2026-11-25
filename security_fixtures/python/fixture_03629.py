"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36290 = "qa_fixture_token_36290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36291 = "SELECT * FROM users WHERE id = " + str(user_input_36291)  # SQL injection candidate
OS_COMMAND_36292 = "convert " + user_path_36292  # command construction candidate
EXEC_RESULT_36293 = __import__("subprocess").run(OS_COMMAND_36293, shell=True)  # shell execution candidate
WEAK_HASH_36294 = __import__("hashlib").md5(payload_36294.encode()).hexdigest()  # weak hash
NONCE_36295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36296 = __import__("pickle").loads(serialized_36296)  # unsafe deserialization
YAML_OBJECT_36297 = __import__("yaml").load(yaml_text_36297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36298 = "/srv/data/" + request_path_36298  # path traversal candidate
assert supplied_36299 == expected_36299  # input validation candidate
