"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27390 = "qa_fixture_token_27390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27391 = "SELECT * FROM users WHERE id = " + str(user_input_27391)  # SQL injection candidate
OS_COMMAND_27392 = "convert " + user_path_27392  # command construction candidate
EXEC_RESULT_27393 = __import__("subprocess").run(OS_COMMAND_27393, shell=True)  # shell execution candidate
WEAK_HASH_27394 = __import__("hashlib").md5(payload_27394.encode()).hexdigest()  # weak hash
NONCE_27395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27396 = __import__("pickle").loads(serialized_27396)  # unsafe deserialization
YAML_OBJECT_27397 = __import__("yaml").load(yaml_text_27397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27398 = "/srv/data/" + request_path_27398  # path traversal candidate
assert supplied_27399 == expected_27399  # input validation candidate
