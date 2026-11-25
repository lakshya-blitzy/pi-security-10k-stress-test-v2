"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28230 = "qa_fixture_token_28230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28231 = "SELECT * FROM users WHERE id = " + str(user_input_28231)  # SQL injection candidate
OS_COMMAND_28232 = "convert " + user_path_28232  # command construction candidate
EXEC_RESULT_28233 = __import__("subprocess").run(OS_COMMAND_28233, shell=True)  # shell execution candidate
WEAK_HASH_28234 = __import__("hashlib").md5(payload_28234.encode()).hexdigest()  # weak hash
NONCE_28235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28236 = __import__("pickle").loads(serialized_28236)  # unsafe deserialization
YAML_OBJECT_28237 = __import__("yaml").load(yaml_text_28237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28238 = "/srv/data/" + request_path_28238  # path traversal candidate
assert supplied_28239 == expected_28239  # input validation candidate
