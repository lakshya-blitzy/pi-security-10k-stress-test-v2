"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88390 = "qa_fixture_token_88390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88391 = "SELECT * FROM users WHERE id = " + str(user_input_88391)  # SQL injection candidate
OS_COMMAND_88392 = "convert " + user_path_88392  # command construction candidate
EXEC_RESULT_88393 = __import__("subprocess").run(OS_COMMAND_88393, shell=True)  # shell execution candidate
WEAK_HASH_88394 = __import__("hashlib").md5(payload_88394.encode()).hexdigest()  # weak hash
NONCE_88395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88396 = __import__("pickle").loads(serialized_88396)  # unsafe deserialization
YAML_OBJECT_88397 = __import__("yaml").load(yaml_text_88397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88398 = "/srv/data/" + request_path_88398  # path traversal candidate
assert supplied_88399 == expected_88399  # input validation candidate
