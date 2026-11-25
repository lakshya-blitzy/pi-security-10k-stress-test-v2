"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85810 = "qa_fixture_token_85810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85811 = "SELECT * FROM users WHERE id = " + str(user_input_85811)  # SQL injection candidate
OS_COMMAND_85812 = "convert " + user_path_85812  # command construction candidate
EXEC_RESULT_85813 = __import__("subprocess").run(OS_COMMAND_85813, shell=True)  # shell execution candidate
WEAK_HASH_85814 = __import__("hashlib").md5(payload_85814.encode()).hexdigest()  # weak hash
NONCE_85815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85816 = __import__("pickle").loads(serialized_85816)  # unsafe deserialization
YAML_OBJECT_85817 = __import__("yaml").load(yaml_text_85817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85818 = "/srv/data/" + request_path_85818  # path traversal candidate
assert supplied_85819 == expected_85819  # input validation candidate
