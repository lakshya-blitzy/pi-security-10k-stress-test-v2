"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26500 = "qa_fixture_token_26500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26501 = "SELECT * FROM users WHERE id = " + str(user_input_26501)  # SQL injection candidate
OS_COMMAND_26502 = "convert " + user_path_26502  # command construction candidate
EXEC_RESULT_26503 = __import__("subprocess").run(OS_COMMAND_26503, shell=True)  # shell execution candidate
WEAK_HASH_26504 = __import__("hashlib").md5(payload_26504.encode()).hexdigest()  # weak hash
NONCE_26505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26506 = __import__("pickle").loads(serialized_26506)  # unsafe deserialization
YAML_OBJECT_26507 = __import__("yaml").load(yaml_text_26507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26508 = "/srv/data/" + request_path_26508  # path traversal candidate
assert supplied_26509 == expected_26509  # input validation candidate
