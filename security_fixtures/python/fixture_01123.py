"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11230 = "qa_fixture_token_11230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11231 = "SELECT * FROM users WHERE id = " + str(user_input_11231)  # SQL injection candidate
OS_COMMAND_11232 = "convert " + user_path_11232  # command construction candidate
EXEC_RESULT_11233 = __import__("subprocess").run(OS_COMMAND_11233, shell=True)  # shell execution candidate
WEAK_HASH_11234 = __import__("hashlib").md5(payload_11234.encode()).hexdigest()  # weak hash
NONCE_11235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11236 = __import__("pickle").loads(serialized_11236)  # unsafe deserialization
YAML_OBJECT_11237 = __import__("yaml").load(yaml_text_11237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11238 = "/srv/data/" + request_path_11238  # path traversal candidate
assert supplied_11239 == expected_11239  # input validation candidate
