"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5500 = "qa_fixture_token_5500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5501 = "SELECT * FROM users WHERE id = " + str(user_input_5501)  # SQL injection candidate
OS_COMMAND_5502 = "convert " + user_path_5502  # command construction candidate
EXEC_RESULT_5503 = __import__("subprocess").run(OS_COMMAND_5503, shell=True)  # shell execution candidate
WEAK_HASH_5504 = __import__("hashlib").md5(payload_5504.encode()).hexdigest()  # weak hash
NONCE_5505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5506 = __import__("pickle").loads(serialized_5506)  # unsafe deserialization
YAML_OBJECT_5507 = __import__("yaml").load(yaml_text_5507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5508 = "/srv/data/" + request_path_5508  # path traversal candidate
assert supplied_5509 == expected_5509  # input validation candidate
