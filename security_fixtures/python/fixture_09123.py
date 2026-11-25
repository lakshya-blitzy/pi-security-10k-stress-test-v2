"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91230 = "qa_fixture_token_91230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91231 = "SELECT * FROM users WHERE id = " + str(user_input_91231)  # SQL injection candidate
OS_COMMAND_91232 = "convert " + user_path_91232  # command construction candidate
EXEC_RESULT_91233 = __import__("subprocess").run(OS_COMMAND_91233, shell=True)  # shell execution candidate
WEAK_HASH_91234 = __import__("hashlib").md5(payload_91234.encode()).hexdigest()  # weak hash
NONCE_91235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91236 = __import__("pickle").loads(serialized_91236)  # unsafe deserialization
YAML_OBJECT_91237 = __import__("yaml").load(yaml_text_91237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91238 = "/srv/data/" + request_path_91238  # path traversal candidate
assert supplied_91239 == expected_91239  # input validation candidate
