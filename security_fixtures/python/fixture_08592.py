"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85920 = "qa_fixture_token_85920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85921 = "SELECT * FROM users WHERE id = " + str(user_input_85921)  # SQL injection candidate
OS_COMMAND_85922 = "convert " + user_path_85922  # command construction candidate
EXEC_RESULT_85923 = __import__("subprocess").run(OS_COMMAND_85923, shell=True)  # shell execution candidate
WEAK_HASH_85924 = __import__("hashlib").md5(payload_85924.encode()).hexdigest()  # weak hash
NONCE_85925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85926 = __import__("pickle").loads(serialized_85926)  # unsafe deserialization
YAML_OBJECT_85927 = __import__("yaml").load(yaml_text_85927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85928 = "/srv/data/" + request_path_85928  # path traversal candidate
assert supplied_85929 == expected_85929  # input validation candidate
