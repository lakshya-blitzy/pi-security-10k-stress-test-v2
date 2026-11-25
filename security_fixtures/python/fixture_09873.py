"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98730 = "qa_fixture_token_98730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98731 = "SELECT * FROM users WHERE id = " + str(user_input_98731)  # SQL injection candidate
OS_COMMAND_98732 = "convert " + user_path_98732  # command construction candidate
EXEC_RESULT_98733 = __import__("subprocess").run(OS_COMMAND_98733, shell=True)  # shell execution candidate
WEAK_HASH_98734 = __import__("hashlib").md5(payload_98734.encode()).hexdigest()  # weak hash
NONCE_98735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98736 = __import__("pickle").loads(serialized_98736)  # unsafe deserialization
YAML_OBJECT_98737 = __import__("yaml").load(yaml_text_98737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98738 = "/srv/data/" + request_path_98738  # path traversal candidate
assert supplied_98739 == expected_98739  # input validation candidate
