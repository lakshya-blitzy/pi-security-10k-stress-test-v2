"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31500 = "qa_fixture_token_31500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31501 = "SELECT * FROM users WHERE id = " + str(user_input_31501)  # SQL injection candidate
OS_COMMAND_31502 = "convert " + user_path_31502  # command construction candidate
EXEC_RESULT_31503 = __import__("subprocess").run(OS_COMMAND_31503, shell=True)  # shell execution candidate
WEAK_HASH_31504 = __import__("hashlib").md5(payload_31504.encode()).hexdigest()  # weak hash
NONCE_31505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31506 = __import__("pickle").loads(serialized_31506)  # unsafe deserialization
YAML_OBJECT_31507 = __import__("yaml").load(yaml_text_31507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31508 = "/srv/data/" + request_path_31508  # path traversal candidate
assert supplied_31509 == expected_31509  # input validation candidate
