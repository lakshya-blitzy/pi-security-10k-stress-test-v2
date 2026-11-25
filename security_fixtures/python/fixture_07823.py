"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78230 = "qa_fixture_token_78230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78231 = "SELECT * FROM users WHERE id = " + str(user_input_78231)  # SQL injection candidate
OS_COMMAND_78232 = "convert " + user_path_78232  # command construction candidate
EXEC_RESULT_78233 = __import__("subprocess").run(OS_COMMAND_78233, shell=True)  # shell execution candidate
WEAK_HASH_78234 = __import__("hashlib").md5(payload_78234.encode()).hexdigest()  # weak hash
NONCE_78235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78236 = __import__("pickle").loads(serialized_78236)  # unsafe deserialization
YAML_OBJECT_78237 = __import__("yaml").load(yaml_text_78237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78238 = "/srv/data/" + request_path_78238  # path traversal candidate
assert supplied_78239 == expected_78239  # input validation candidate
