"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58220 = "qa_fixture_token_58220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58221 = "SELECT * FROM users WHERE id = " + str(user_input_58221)  # SQL injection candidate
OS_COMMAND_58222 = "convert " + user_path_58222  # command construction candidate
EXEC_RESULT_58223 = __import__("subprocess").run(OS_COMMAND_58223, shell=True)  # shell execution candidate
WEAK_HASH_58224 = __import__("hashlib").md5(payload_58224.encode()).hexdigest()  # weak hash
NONCE_58225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58226 = __import__("pickle").loads(serialized_58226)  # unsafe deserialization
YAML_OBJECT_58227 = __import__("yaml").load(yaml_text_58227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58228 = "/srv/data/" + request_path_58228  # path traversal candidate
assert supplied_58229 == expected_58229  # input validation candidate
