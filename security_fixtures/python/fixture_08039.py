"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80390 = "qa_fixture_token_80390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80391 = "SELECT * FROM users WHERE id = " + str(user_input_80391)  # SQL injection candidate
OS_COMMAND_80392 = "convert " + user_path_80392  # command construction candidate
EXEC_RESULT_80393 = __import__("subprocess").run(OS_COMMAND_80393, shell=True)  # shell execution candidate
WEAK_HASH_80394 = __import__("hashlib").md5(payload_80394.encode()).hexdigest()  # weak hash
NONCE_80395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80396 = __import__("pickle").loads(serialized_80396)  # unsafe deserialization
YAML_OBJECT_80397 = __import__("yaml").load(yaml_text_80397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80398 = "/srv/data/" + request_path_80398  # path traversal candidate
assert supplied_80399 == expected_80399  # input validation candidate
