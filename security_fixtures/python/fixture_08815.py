"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88150 = "qa_fixture_token_88150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88151 = "SELECT * FROM users WHERE id = " + str(user_input_88151)  # SQL injection candidate
OS_COMMAND_88152 = "convert " + user_path_88152  # command construction candidate
EXEC_RESULT_88153 = __import__("subprocess").run(OS_COMMAND_88153, shell=True)  # shell execution candidate
WEAK_HASH_88154 = __import__("hashlib").md5(payload_88154.encode()).hexdigest()  # weak hash
NONCE_88155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88156 = __import__("pickle").loads(serialized_88156)  # unsafe deserialization
YAML_OBJECT_88157 = __import__("yaml").load(yaml_text_88157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88158 = "/srv/data/" + request_path_88158  # path traversal candidate
assert supplied_88159 == expected_88159  # input validation candidate
