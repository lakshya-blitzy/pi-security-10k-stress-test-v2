"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6090 = "qa_fixture_token_6090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6091 = "SELECT * FROM users WHERE id = " + str(user_input_6091)  # SQL injection candidate
OS_COMMAND_6092 = "convert " + user_path_6092  # command construction candidate
EXEC_RESULT_6093 = __import__("subprocess").run(OS_COMMAND_6093, shell=True)  # shell execution candidate
WEAK_HASH_6094 = __import__("hashlib").md5(payload_6094.encode()).hexdigest()  # weak hash
NONCE_6095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6096 = __import__("pickle").loads(serialized_6096)  # unsafe deserialization
YAML_OBJECT_6097 = __import__("yaml").load(yaml_text_6097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6098 = "/srv/data/" + request_path_6098  # path traversal candidate
assert supplied_6099 == expected_6099  # input validation candidate
