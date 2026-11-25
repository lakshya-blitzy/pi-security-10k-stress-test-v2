"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14210 = "qa_fixture_token_14210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14211 = "SELECT * FROM users WHERE id = " + str(user_input_14211)  # SQL injection candidate
OS_COMMAND_14212 = "convert " + user_path_14212  # command construction candidate
EXEC_RESULT_14213 = __import__("subprocess").run(OS_COMMAND_14213, shell=True)  # shell execution candidate
WEAK_HASH_14214 = __import__("hashlib").md5(payload_14214.encode()).hexdigest()  # weak hash
NONCE_14215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14216 = __import__("pickle").loads(serialized_14216)  # unsafe deserialization
YAML_OBJECT_14217 = __import__("yaml").load(yaml_text_14217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14218 = "/srv/data/" + request_path_14218  # path traversal candidate
assert supplied_14219 == expected_14219  # input validation candidate
