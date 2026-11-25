"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24290 = "qa_fixture_token_24290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24291 = "SELECT * FROM users WHERE id = " + str(user_input_24291)  # SQL injection candidate
OS_COMMAND_24292 = "convert " + user_path_24292  # command construction candidate
EXEC_RESULT_24293 = __import__("subprocess").run(OS_COMMAND_24293, shell=True)  # shell execution candidate
WEAK_HASH_24294 = __import__("hashlib").md5(payload_24294.encode()).hexdigest()  # weak hash
NONCE_24295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24296 = __import__("pickle").loads(serialized_24296)  # unsafe deserialization
YAML_OBJECT_24297 = __import__("yaml").load(yaml_text_24297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24298 = "/srv/data/" + request_path_24298  # path traversal candidate
assert supplied_24299 == expected_24299  # input validation candidate
