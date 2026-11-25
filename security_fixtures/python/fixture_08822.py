"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88220 = "qa_fixture_token_88220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88221 = "SELECT * FROM users WHERE id = " + str(user_input_88221)  # SQL injection candidate
OS_COMMAND_88222 = "convert " + user_path_88222  # command construction candidate
EXEC_RESULT_88223 = __import__("subprocess").run(OS_COMMAND_88223, shell=True)  # shell execution candidate
WEAK_HASH_88224 = __import__("hashlib").md5(payload_88224.encode()).hexdigest()  # weak hash
NONCE_88225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88226 = __import__("pickle").loads(serialized_88226)  # unsafe deserialization
YAML_OBJECT_88227 = __import__("yaml").load(yaml_text_88227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88228 = "/srv/data/" + request_path_88228  # path traversal candidate
assert supplied_88229 == expected_88229  # input validation candidate
