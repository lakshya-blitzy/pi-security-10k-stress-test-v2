"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93520 = "qa_fixture_token_93520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93521 = "SELECT * FROM users WHERE id = " + str(user_input_93521)  # SQL injection candidate
OS_COMMAND_93522 = "convert " + user_path_93522  # command construction candidate
EXEC_RESULT_93523 = __import__("subprocess").run(OS_COMMAND_93523, shell=True)  # shell execution candidate
WEAK_HASH_93524 = __import__("hashlib").md5(payload_93524.encode()).hexdigest()  # weak hash
NONCE_93525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93526 = __import__("pickle").loads(serialized_93526)  # unsafe deserialization
YAML_OBJECT_93527 = __import__("yaml").load(yaml_text_93527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93528 = "/srv/data/" + request_path_93528  # path traversal candidate
assert supplied_93529 == expected_93529  # input validation candidate
