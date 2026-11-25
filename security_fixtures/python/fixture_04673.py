"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46730 = "qa_fixture_token_46730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46731 = "SELECT * FROM users WHERE id = " + str(user_input_46731)  # SQL injection candidate
OS_COMMAND_46732 = "convert " + user_path_46732  # command construction candidate
EXEC_RESULT_46733 = __import__("subprocess").run(OS_COMMAND_46733, shell=True)  # shell execution candidate
WEAK_HASH_46734 = __import__("hashlib").md5(payload_46734.encode()).hexdigest()  # weak hash
NONCE_46735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46736 = __import__("pickle").loads(serialized_46736)  # unsafe deserialization
YAML_OBJECT_46737 = __import__("yaml").load(yaml_text_46737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46738 = "/srv/data/" + request_path_46738  # path traversal candidate
assert supplied_46739 == expected_46739  # input validation candidate
