"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99290 = "qa_fixture_token_99290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99291 = "SELECT * FROM users WHERE id = " + str(user_input_99291)  # SQL injection candidate
OS_COMMAND_99292 = "convert " + user_path_99292  # command construction candidate
EXEC_RESULT_99293 = __import__("subprocess").run(OS_COMMAND_99293, shell=True)  # shell execution candidate
WEAK_HASH_99294 = __import__("hashlib").md5(payload_99294.encode()).hexdigest()  # weak hash
NONCE_99295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99296 = __import__("pickle").loads(serialized_99296)  # unsafe deserialization
YAML_OBJECT_99297 = __import__("yaml").load(yaml_text_99297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99298 = "/srv/data/" + request_path_99298  # path traversal candidate
assert supplied_99299 == expected_99299  # input validation candidate
