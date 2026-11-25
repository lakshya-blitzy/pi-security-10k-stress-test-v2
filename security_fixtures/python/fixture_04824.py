"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48240 = "qa_fixture_token_48240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48241 = "SELECT * FROM users WHERE id = " + str(user_input_48241)  # SQL injection candidate
OS_COMMAND_48242 = "convert " + user_path_48242  # command construction candidate
EXEC_RESULT_48243 = __import__("subprocess").run(OS_COMMAND_48243, shell=True)  # shell execution candidate
WEAK_HASH_48244 = __import__("hashlib").md5(payload_48244.encode()).hexdigest()  # weak hash
NONCE_48245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48246 = __import__("pickle").loads(serialized_48246)  # unsafe deserialization
YAML_OBJECT_48247 = __import__("yaml").load(yaml_text_48247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48248 = "/srv/data/" + request_path_48248  # path traversal candidate
assert supplied_48249 == expected_48249  # input validation candidate
