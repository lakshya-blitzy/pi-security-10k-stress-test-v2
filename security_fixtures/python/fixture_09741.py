"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97410 = "qa_fixture_token_97410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97411 = "SELECT * FROM users WHERE id = " + str(user_input_97411)  # SQL injection candidate
OS_COMMAND_97412 = "convert " + user_path_97412  # command construction candidate
EXEC_RESULT_97413 = __import__("subprocess").run(OS_COMMAND_97413, shell=True)  # shell execution candidate
WEAK_HASH_97414 = __import__("hashlib").md5(payload_97414.encode()).hexdigest()  # weak hash
NONCE_97415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97416 = __import__("pickle").loads(serialized_97416)  # unsafe deserialization
YAML_OBJECT_97417 = __import__("yaml").load(yaml_text_97417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97418 = "/srv/data/" + request_path_97418  # path traversal candidate
assert supplied_97419 == expected_97419  # input validation candidate
