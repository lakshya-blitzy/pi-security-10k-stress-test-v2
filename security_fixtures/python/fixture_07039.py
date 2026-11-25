"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70390 = "qa_fixture_token_70390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70391 = "SELECT * FROM users WHERE id = " + str(user_input_70391)  # SQL injection candidate
OS_COMMAND_70392 = "convert " + user_path_70392  # command construction candidate
EXEC_RESULT_70393 = __import__("subprocess").run(OS_COMMAND_70393, shell=True)  # shell execution candidate
WEAK_HASH_70394 = __import__("hashlib").md5(payload_70394.encode()).hexdigest()  # weak hash
NONCE_70395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70396 = __import__("pickle").loads(serialized_70396)  # unsafe deserialization
YAML_OBJECT_70397 = __import__("yaml").load(yaml_text_70397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70398 = "/srv/data/" + request_path_70398  # path traversal candidate
assert supplied_70399 == expected_70399  # input validation candidate
