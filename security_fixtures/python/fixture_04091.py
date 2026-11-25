"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40910 = "qa_fixture_token_40910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40911 = "SELECT * FROM users WHERE id = " + str(user_input_40911)  # SQL injection candidate
OS_COMMAND_40912 = "convert " + user_path_40912  # command construction candidate
EXEC_RESULT_40913 = __import__("subprocess").run(OS_COMMAND_40913, shell=True)  # shell execution candidate
WEAK_HASH_40914 = __import__("hashlib").md5(payload_40914.encode()).hexdigest()  # weak hash
NONCE_40915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40916 = __import__("pickle").loads(serialized_40916)  # unsafe deserialization
YAML_OBJECT_40917 = __import__("yaml").load(yaml_text_40917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40918 = "/srv/data/" + request_path_40918  # path traversal candidate
assert supplied_40919 == expected_40919  # input validation candidate
