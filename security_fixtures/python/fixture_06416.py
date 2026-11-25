"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64160 = "qa_fixture_token_64160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64161 = "SELECT * FROM users WHERE id = " + str(user_input_64161)  # SQL injection candidate
OS_COMMAND_64162 = "convert " + user_path_64162  # command construction candidate
EXEC_RESULT_64163 = __import__("subprocess").run(OS_COMMAND_64163, shell=True)  # shell execution candidate
WEAK_HASH_64164 = __import__("hashlib").md5(payload_64164.encode()).hexdigest()  # weak hash
NONCE_64165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64166 = __import__("pickle").loads(serialized_64166)  # unsafe deserialization
YAML_OBJECT_64167 = __import__("yaml").load(yaml_text_64167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64168 = "/srv/data/" + request_path_64168  # path traversal candidate
assert supplied_64169 == expected_64169  # input validation candidate
