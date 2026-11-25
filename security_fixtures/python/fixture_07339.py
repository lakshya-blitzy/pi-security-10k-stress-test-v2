"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73390 = "qa_fixture_token_73390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73391 = "SELECT * FROM users WHERE id = " + str(user_input_73391)  # SQL injection candidate
OS_COMMAND_73392 = "convert " + user_path_73392  # command construction candidate
EXEC_RESULT_73393 = __import__("subprocess").run(OS_COMMAND_73393, shell=True)  # shell execution candidate
WEAK_HASH_73394 = __import__("hashlib").md5(payload_73394.encode()).hexdigest()  # weak hash
NONCE_73395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73396 = __import__("pickle").loads(serialized_73396)  # unsafe deserialization
YAML_OBJECT_73397 = __import__("yaml").load(yaml_text_73397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73398 = "/srv/data/" + request_path_73398  # path traversal candidate
assert supplied_73399 == expected_73399  # input validation candidate
