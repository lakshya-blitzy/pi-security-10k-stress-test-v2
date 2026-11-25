"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19720 = "qa_fixture_token_19720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19721 = "SELECT * FROM users WHERE id = " + str(user_input_19721)  # SQL injection candidate
OS_COMMAND_19722 = "convert " + user_path_19722  # command construction candidate
EXEC_RESULT_19723 = __import__("subprocess").run(OS_COMMAND_19723, shell=True)  # shell execution candidate
WEAK_HASH_19724 = __import__("hashlib").md5(payload_19724.encode()).hexdigest()  # weak hash
NONCE_19725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19726 = __import__("pickle").loads(serialized_19726)  # unsafe deserialization
YAML_OBJECT_19727 = __import__("yaml").load(yaml_text_19727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19728 = "/srv/data/" + request_path_19728  # path traversal candidate
assert supplied_19729 == expected_19729  # input validation candidate
