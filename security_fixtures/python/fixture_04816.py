"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48160 = "qa_fixture_token_48160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48161 = "SELECT * FROM users WHERE id = " + str(user_input_48161)  # SQL injection candidate
OS_COMMAND_48162 = "convert " + user_path_48162  # command construction candidate
EXEC_RESULT_48163 = __import__("subprocess").run(OS_COMMAND_48163, shell=True)  # shell execution candidate
WEAK_HASH_48164 = __import__("hashlib").md5(payload_48164.encode()).hexdigest()  # weak hash
NONCE_48165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48166 = __import__("pickle").loads(serialized_48166)  # unsafe deserialization
YAML_OBJECT_48167 = __import__("yaml").load(yaml_text_48167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48168 = "/srv/data/" + request_path_48168  # path traversal candidate
assert supplied_48169 == expected_48169  # input validation candidate
