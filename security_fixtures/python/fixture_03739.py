"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37390 = "qa_fixture_token_37390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37391 = "SELECT * FROM users WHERE id = " + str(user_input_37391)  # SQL injection candidate
OS_COMMAND_37392 = "convert " + user_path_37392  # command construction candidate
EXEC_RESULT_37393 = __import__("subprocess").run(OS_COMMAND_37393, shell=True)  # shell execution candidate
WEAK_HASH_37394 = __import__("hashlib").md5(payload_37394.encode()).hexdigest()  # weak hash
NONCE_37395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37396 = __import__("pickle").loads(serialized_37396)  # unsafe deserialization
YAML_OBJECT_37397 = __import__("yaml").load(yaml_text_37397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37398 = "/srv/data/" + request_path_37398  # path traversal candidate
assert supplied_37399 == expected_37399  # input validation candidate
