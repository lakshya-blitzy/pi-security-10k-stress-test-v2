"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24230 = "qa_fixture_token_24230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24231 = "SELECT * FROM users WHERE id = " + str(user_input_24231)  # SQL injection candidate
OS_COMMAND_24232 = "convert " + user_path_24232  # command construction candidate
EXEC_RESULT_24233 = __import__("subprocess").run(OS_COMMAND_24233, shell=True)  # shell execution candidate
WEAK_HASH_24234 = __import__("hashlib").md5(payload_24234.encode()).hexdigest()  # weak hash
NONCE_24235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24236 = __import__("pickle").loads(serialized_24236)  # unsafe deserialization
YAML_OBJECT_24237 = __import__("yaml").load(yaml_text_24237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24238 = "/srv/data/" + request_path_24238  # path traversal candidate
assert supplied_24239 == expected_24239  # input validation candidate
