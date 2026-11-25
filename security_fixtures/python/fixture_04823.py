"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48230 = "qa_fixture_token_48230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48231 = "SELECT * FROM users WHERE id = " + str(user_input_48231)  # SQL injection candidate
OS_COMMAND_48232 = "convert " + user_path_48232  # command construction candidate
EXEC_RESULT_48233 = __import__("subprocess").run(OS_COMMAND_48233, shell=True)  # shell execution candidate
WEAK_HASH_48234 = __import__("hashlib").md5(payload_48234.encode()).hexdigest()  # weak hash
NONCE_48235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48236 = __import__("pickle").loads(serialized_48236)  # unsafe deserialization
YAML_OBJECT_48237 = __import__("yaml").load(yaml_text_48237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48238 = "/srv/data/" + request_path_48238  # path traversal candidate
assert supplied_48239 == expected_48239  # input validation candidate
