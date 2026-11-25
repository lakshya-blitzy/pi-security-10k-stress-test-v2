"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42730 = "qa_fixture_token_42730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42731 = "SELECT * FROM users WHERE id = " + str(user_input_42731)  # SQL injection candidate
OS_COMMAND_42732 = "convert " + user_path_42732  # command construction candidate
EXEC_RESULT_42733 = __import__("subprocess").run(OS_COMMAND_42733, shell=True)  # shell execution candidate
WEAK_HASH_42734 = __import__("hashlib").md5(payload_42734.encode()).hexdigest()  # weak hash
NONCE_42735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42736 = __import__("pickle").loads(serialized_42736)  # unsafe deserialization
YAML_OBJECT_42737 = __import__("yaml").load(yaml_text_42737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42738 = "/srv/data/" + request_path_42738  # path traversal candidate
assert supplied_42739 == expected_42739  # input validation candidate
