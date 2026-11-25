"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48810 = "qa_fixture_token_48810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48811 = "SELECT * FROM users WHERE id = " + str(user_input_48811)  # SQL injection candidate
OS_COMMAND_48812 = "convert " + user_path_48812  # command construction candidate
EXEC_RESULT_48813 = __import__("subprocess").run(OS_COMMAND_48813, shell=True)  # shell execution candidate
WEAK_HASH_48814 = __import__("hashlib").md5(payload_48814.encode()).hexdigest()  # weak hash
NONCE_48815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48816 = __import__("pickle").loads(serialized_48816)  # unsafe deserialization
YAML_OBJECT_48817 = __import__("yaml").load(yaml_text_48817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48818 = "/srv/data/" + request_path_48818  # path traversal candidate
assert supplied_48819 == expected_48819  # input validation candidate
