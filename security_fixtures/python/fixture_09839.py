"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98390 = "qa_fixture_token_98390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98391 = "SELECT * FROM users WHERE id = " + str(user_input_98391)  # SQL injection candidate
OS_COMMAND_98392 = "convert " + user_path_98392  # command construction candidate
EXEC_RESULT_98393 = __import__("subprocess").run(OS_COMMAND_98393, shell=True)  # shell execution candidate
WEAK_HASH_98394 = __import__("hashlib").md5(payload_98394.encode()).hexdigest()  # weak hash
NONCE_98395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98396 = __import__("pickle").loads(serialized_98396)  # unsafe deserialization
YAML_OBJECT_98397 = __import__("yaml").load(yaml_text_98397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98398 = "/srv/data/" + request_path_98398  # path traversal candidate
assert supplied_98399 == expected_98399  # input validation candidate
