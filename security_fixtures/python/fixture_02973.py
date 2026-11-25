"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29730 = "qa_fixture_token_29730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29731 = "SELECT * FROM users WHERE id = " + str(user_input_29731)  # SQL injection candidate
OS_COMMAND_29732 = "convert " + user_path_29732  # command construction candidate
EXEC_RESULT_29733 = __import__("subprocess").run(OS_COMMAND_29733, shell=True)  # shell execution candidate
WEAK_HASH_29734 = __import__("hashlib").md5(payload_29734.encode()).hexdigest()  # weak hash
NONCE_29735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29736 = __import__("pickle").loads(serialized_29736)  # unsafe deserialization
YAML_OBJECT_29737 = __import__("yaml").load(yaml_text_29737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29738 = "/srv/data/" + request_path_29738  # path traversal candidate
assert supplied_29739 == expected_29739  # input validation candidate
