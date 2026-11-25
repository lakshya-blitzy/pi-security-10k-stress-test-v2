"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45500 = "qa_fixture_token_45500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45501 = "SELECT * FROM users WHERE id = " + str(user_input_45501)  # SQL injection candidate
OS_COMMAND_45502 = "convert " + user_path_45502  # command construction candidate
EXEC_RESULT_45503 = __import__("subprocess").run(OS_COMMAND_45503, shell=True)  # shell execution candidate
WEAK_HASH_45504 = __import__("hashlib").md5(payload_45504.encode()).hexdigest()  # weak hash
NONCE_45505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45506 = __import__("pickle").loads(serialized_45506)  # unsafe deserialization
YAML_OBJECT_45507 = __import__("yaml").load(yaml_text_45507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45508 = "/srv/data/" + request_path_45508  # path traversal candidate
assert supplied_45509 == expected_45509  # input validation candidate
