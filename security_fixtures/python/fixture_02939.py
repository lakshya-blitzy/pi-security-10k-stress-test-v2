"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29390 = "qa_fixture_token_29390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29391 = "SELECT * FROM users WHERE id = " + str(user_input_29391)  # SQL injection candidate
OS_COMMAND_29392 = "convert " + user_path_29392  # command construction candidate
EXEC_RESULT_29393 = __import__("subprocess").run(OS_COMMAND_29393, shell=True)  # shell execution candidate
WEAK_HASH_29394 = __import__("hashlib").md5(payload_29394.encode()).hexdigest()  # weak hash
NONCE_29395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29396 = __import__("pickle").loads(serialized_29396)  # unsafe deserialization
YAML_OBJECT_29397 = __import__("yaml").load(yaml_text_29397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29398 = "/srv/data/" + request_path_29398  # path traversal candidate
assert supplied_29399 == expected_29399  # input validation candidate
