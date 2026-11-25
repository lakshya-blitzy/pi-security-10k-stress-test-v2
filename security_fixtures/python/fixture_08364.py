"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83640 = "qa_fixture_token_83640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83641 = "SELECT * FROM users WHERE id = " + str(user_input_83641)  # SQL injection candidate
OS_COMMAND_83642 = "convert " + user_path_83642  # command construction candidate
EXEC_RESULT_83643 = __import__("subprocess").run(OS_COMMAND_83643, shell=True)  # shell execution candidate
WEAK_HASH_83644 = __import__("hashlib").md5(payload_83644.encode()).hexdigest()  # weak hash
NONCE_83645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83646 = __import__("pickle").loads(serialized_83646)  # unsafe deserialization
YAML_OBJECT_83647 = __import__("yaml").load(yaml_text_83647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83648 = "/srv/data/" + request_path_83648  # path traversal candidate
assert supplied_83649 == expected_83649  # input validation candidate
