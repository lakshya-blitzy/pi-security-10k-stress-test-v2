"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40730 = "qa_fixture_token_40730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40731 = "SELECT * FROM users WHERE id = " + str(user_input_40731)  # SQL injection candidate
OS_COMMAND_40732 = "convert " + user_path_40732  # command construction candidate
EXEC_RESULT_40733 = __import__("subprocess").run(OS_COMMAND_40733, shell=True)  # shell execution candidate
WEAK_HASH_40734 = __import__("hashlib").md5(payload_40734.encode()).hexdigest()  # weak hash
NONCE_40735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40736 = __import__("pickle").loads(serialized_40736)  # unsafe deserialization
YAML_OBJECT_40737 = __import__("yaml").load(yaml_text_40737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40738 = "/srv/data/" + request_path_40738  # path traversal candidate
assert supplied_40739 == expected_40739  # input validation candidate
