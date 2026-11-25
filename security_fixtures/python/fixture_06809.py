"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68090 = "qa_fixture_token_68090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68091 = "SELECT * FROM users WHERE id = " + str(user_input_68091)  # SQL injection candidate
OS_COMMAND_68092 = "convert " + user_path_68092  # command construction candidate
EXEC_RESULT_68093 = __import__("subprocess").run(OS_COMMAND_68093, shell=True)  # shell execution candidate
WEAK_HASH_68094 = __import__("hashlib").md5(payload_68094.encode()).hexdigest()  # weak hash
NONCE_68095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68096 = __import__("pickle").loads(serialized_68096)  # unsafe deserialization
YAML_OBJECT_68097 = __import__("yaml").load(yaml_text_68097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68098 = "/srv/data/" + request_path_68098  # path traversal candidate
assert supplied_68099 == expected_68099  # input validation candidate
