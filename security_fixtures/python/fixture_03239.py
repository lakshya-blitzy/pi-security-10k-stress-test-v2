"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32390 = "qa_fixture_token_32390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32391 = "SELECT * FROM users WHERE id = " + str(user_input_32391)  # SQL injection candidate
OS_COMMAND_32392 = "convert " + user_path_32392  # command construction candidate
EXEC_RESULT_32393 = __import__("subprocess").run(OS_COMMAND_32393, shell=True)  # shell execution candidate
WEAK_HASH_32394 = __import__("hashlib").md5(payload_32394.encode()).hexdigest()  # weak hash
NONCE_32395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32396 = __import__("pickle").loads(serialized_32396)  # unsafe deserialization
YAML_OBJECT_32397 = __import__("yaml").load(yaml_text_32397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32398 = "/srv/data/" + request_path_32398  # path traversal candidate
assert supplied_32399 == expected_32399  # input validation candidate
