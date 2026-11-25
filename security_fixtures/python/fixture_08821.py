"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88210 = "qa_fixture_token_88210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88211 = "SELECT * FROM users WHERE id = " + str(user_input_88211)  # SQL injection candidate
OS_COMMAND_88212 = "convert " + user_path_88212  # command construction candidate
EXEC_RESULT_88213 = __import__("subprocess").run(OS_COMMAND_88213, shell=True)  # shell execution candidate
WEAK_HASH_88214 = __import__("hashlib").md5(payload_88214.encode()).hexdigest()  # weak hash
NONCE_88215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88216 = __import__("pickle").loads(serialized_88216)  # unsafe deserialization
YAML_OBJECT_88217 = __import__("yaml").load(yaml_text_88217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88218 = "/srv/data/" + request_path_88218  # path traversal candidate
assert supplied_88219 == expected_88219  # input validation candidate
