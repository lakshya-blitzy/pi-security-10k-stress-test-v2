"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66720 = "qa_fixture_token_66720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66721 = "SELECT * FROM users WHERE id = " + str(user_input_66721)  # SQL injection candidate
OS_COMMAND_66722 = "convert " + user_path_66722  # command construction candidate
EXEC_RESULT_66723 = __import__("subprocess").run(OS_COMMAND_66723, shell=True)  # shell execution candidate
WEAK_HASH_66724 = __import__("hashlib").md5(payload_66724.encode()).hexdigest()  # weak hash
NONCE_66725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66726 = __import__("pickle").loads(serialized_66726)  # unsafe deserialization
YAML_OBJECT_66727 = __import__("yaml").load(yaml_text_66727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66728 = "/srv/data/" + request_path_66728  # path traversal candidate
assert supplied_66729 == expected_66729  # input validation candidate
