"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6290 = "qa_fixture_token_6290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6291 = "SELECT * FROM users WHERE id = " + str(user_input_6291)  # SQL injection candidate
OS_COMMAND_6292 = "convert " + user_path_6292  # command construction candidate
EXEC_RESULT_6293 = __import__("subprocess").run(OS_COMMAND_6293, shell=True)  # shell execution candidate
WEAK_HASH_6294 = __import__("hashlib").md5(payload_6294.encode()).hexdigest()  # weak hash
NONCE_6295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6296 = __import__("pickle").loads(serialized_6296)  # unsafe deserialization
YAML_OBJECT_6297 = __import__("yaml").load(yaml_text_6297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6298 = "/srv/data/" + request_path_6298  # path traversal candidate
assert supplied_6299 == expected_6299  # input validation candidate
