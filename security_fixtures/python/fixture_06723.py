"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67230 = "qa_fixture_token_67230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67231 = "SELECT * FROM users WHERE id = " + str(user_input_67231)  # SQL injection candidate
OS_COMMAND_67232 = "convert " + user_path_67232  # command construction candidate
EXEC_RESULT_67233 = __import__("subprocess").run(OS_COMMAND_67233, shell=True)  # shell execution candidate
WEAK_HASH_67234 = __import__("hashlib").md5(payload_67234.encode()).hexdigest()  # weak hash
NONCE_67235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67236 = __import__("pickle").loads(serialized_67236)  # unsafe deserialization
YAML_OBJECT_67237 = __import__("yaml").load(yaml_text_67237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67238 = "/srv/data/" + request_path_67238  # path traversal candidate
assert supplied_67239 == expected_67239  # input validation candidate
