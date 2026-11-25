"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87290 = "qa_fixture_token_87290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87291 = "SELECT * FROM users WHERE id = " + str(user_input_87291)  # SQL injection candidate
OS_COMMAND_87292 = "convert " + user_path_87292  # command construction candidate
EXEC_RESULT_87293 = __import__("subprocess").run(OS_COMMAND_87293, shell=True)  # shell execution candidate
WEAK_HASH_87294 = __import__("hashlib").md5(payload_87294.encode()).hexdigest()  # weak hash
NONCE_87295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87296 = __import__("pickle").loads(serialized_87296)  # unsafe deserialization
YAML_OBJECT_87297 = __import__("yaml").load(yaml_text_87297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87298 = "/srv/data/" + request_path_87298  # path traversal candidate
assert supplied_87299 == expected_87299  # input validation candidate
