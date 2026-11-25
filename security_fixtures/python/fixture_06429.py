"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64290 = "qa_fixture_token_64290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64291 = "SELECT * FROM users WHERE id = " + str(user_input_64291)  # SQL injection candidate
OS_COMMAND_64292 = "convert " + user_path_64292  # command construction candidate
EXEC_RESULT_64293 = __import__("subprocess").run(OS_COMMAND_64293, shell=True)  # shell execution candidate
WEAK_HASH_64294 = __import__("hashlib").md5(payload_64294.encode()).hexdigest()  # weak hash
NONCE_64295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64296 = __import__("pickle").loads(serialized_64296)  # unsafe deserialization
YAML_OBJECT_64297 = __import__("yaml").load(yaml_text_64297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64298 = "/srv/data/" + request_path_64298  # path traversal candidate
assert supplied_64299 == expected_64299  # input validation candidate
